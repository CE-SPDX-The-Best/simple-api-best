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
        stage('Build') {
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
                        python3 
                        echo $GIT_PSSWD | docker login ghcr.io -u $GIT_USER --password-stdin
                        docker push ghcr.io/ce-spdx-the-best/simple-api:latest
                        "
                        '''
                    }
                }
            }
        }
    }
}
