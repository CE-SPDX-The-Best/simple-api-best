pipeline {
    agent any
    // triggers {
    //     pollSCM('* * * * *') // Poll every 1 minutes; adjust as needed
    // }
    stages {
        stage('Checkout') {
            steps {
                // Clone or pull the latest code
                checkout scm
            }
        }
        stage('VM1') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'muyumq-github', passwordVariable: 'GIT_PSSWD', usernameVariable: 'GIT_USER')]) {
                    sshagent (credentials: ['ssh-key']) {
                        sh '''
                        ssh -o StrictHostKeyChecking=no admin@192.168.1.56 "
                        # ไปที่ home directory
                        cd ~
                        # เข้าไปที่ project
                        cd simple-api
                        docker compose down
                        git pull origin main
                        mv ../wait-for-it.sh .
                        
                        # สร้าง/อัปเดต image และ start service
                        docker compose up -d --build
                        ./wait-for-it.sh localhost:5000 -t 30 -- echo "Service is up"
                        simple-env/bin/pip install -r requirements.txt
                        simple-env/bin/python3 -m unittest unit_test.py
                        cd ~/simple-api-robot
                        git pull origin main
                        robot-env/bin/pip install -r requirements.txt
                        robot-env/bin/robot robot-test.robot
                        echo $GIT_PSSWD | docker login ghcr.io -u $GIT_USER --password-stdin
                        docker tag simple-api:latest ghcr.io/ce-spdx-the-best/simple-api:latest
                        docker push ghcr.io/ce-spdx-the-best/simple-api:latest
                        "
                        '''
                    }
                }
            }
        }
        stage('VM2') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'muyumq-github', passwordVariable: 'GIT_PSSWD', usernameVariable: 'GIT_USER')]) {
                    sshagent (credentials: ['ssh-key']) {
                        sh '''
                        ssh -o StrictHostKeyChecking=no admin@192.168.1.61 "
                        echo $GIT_PSSWD | docker login ghcr.io -u $GIT_USER --password-stdin
                        docker pull ghcr.io/ce-spdx-the-best/simple-api:latest
                        docker stop simple-api || true
                        docker run -d -p 5000:5000 --name simple-api ghcr.io/ce-spdx-the-best/simple-api:latest
                        ./wait-for-it.sh localhost:5000 -t 30 -- echo "Service is up"
                        "
                        '''
                    }
                }
            }
        }
    }
}
