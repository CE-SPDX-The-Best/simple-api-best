pipeline {
    agent { label 'build'}

    stages {
        stage('Checkout') {
            steps {
                // checkout scm
                git credentialsId: 'muyumq-github', url: 'https://github.com/CE-SPDX-The-Best/simple-api-best.git', branch: 'main'
            }
        }

        stage('Setup Environment & Install Dependencies') {
            steps {
                echo "1. Creating Python virtual environment (venv)..."
                // สร้างโฟลเดอร์ venv
                sh 'python3 -m venv venv' 

                echo "2. Activating venv and installing requirements..."
                // รันคำสั่งใน shell session เดียว
                // 'source' จะ activate venv
                // 'pip install' จะติดตั้งลงใน venv นั้นทันที
                sh '''
                   source venv/bin/activate
                   pip install -r requirements.txt
                   echo "--- Packages installed in venv: ---"
                   pip list
                '''
            }
        }
        
        // stage('Build-Run Web') {
        //     steps {
        //         sh 'docker compose up -d --build'
        //         sh 'sleep 5'

        //     }
        // }

//         stage('VM2') {
//             steps {
//                 withCredentials([usernamePassword(credentialsId: 'muyumq-github', passwordVariable: 'GIT_PSSWD', usernameVariable: 'GIT_USER'),
//                                 sshUserPrivateKey(credentialsId: 'ssh-key', keyFileVariable: 'SSH_KEY', usernameVariable: 'SSH_USER')]) {
//                     sshagent (credentials: ['ssh-key']) {
//                         sh '''
//                         ssh -o StrictHostKeyChecking=no $SSH_USER@192.168.56.105 "
//                         # ไปที่ home directory
//                         cd ~
//                         # เข้าไปที่ project
//                         cd simple-api
//                         docker compose down
//                         git pull origin main
                        
//                         # สร้าง/อัปเดต image และ start service
//                         docker compose up -d --build
//                         ./wait-for-it.sh localhost:5000 -t 30 -- echo "Service is up"
//                         docker image prune -a -f
//                         simple-env/bin/pip install -r requirements.txt
//                         simple-env/bin/python3 -m unittest unit_test.py
//                         cd ~/simple-api-robot
//                         git pull origin main
//                         robot-env/bin/pip install -r requirements.txt
//                         robot-env/bin/robot robot-test.robot
//                         echo $GIT_PSSWD | docker login ghcr.io -u $GIT_USER --password-stdin
//                         docker tag simple-api:latest ghcr.io/ce-spdx-the-best/simple-api:latest
//                         docker push ghcr.io/ce-spdx-the-best/simple-api:latest
//                         "
//                         '''
//                     }
//                 }
//             }
//         }
//         stage('VM3') {
//             steps {
//                 withCredentials([usernamePassword(credentialsId: 'muyumq-github', passwordVariable: 'GIT_PSSWD', usernameVariable: 'GIT_USER'),
//                                 sshUserPrivateKey(credentialsId: 'ssh-key', keyFileVariable: 'SSH_KEY', usernameVariable: 'SSH_USER')]) {
//                     sshagent (credentials: ['ssh-key']) {
//                         sh '''
//                         ssh -o StrictHostKeyChecking=no $SSH_USER@192.168.56.106 "
//                         echo $GIT_PSSWD | docker login ghcr.io -u $GIT_USER --password-stdin
//                         docker stop simple-api || true
//                         docker rmi ghcr.io/ce-spdx-the-best/simple-api:latest || true
//                         docker pull ghcr.io/ce-spdx-the-best/simple-api:latest
//                         docker run -d -p 5000:5000 --name simple-api --rm ghcr.io/ce-spdx-the-best/simple-api:latest
//                         ./wait-for-it.sh localhost:5000 -t 30 -- echo "Service is up"
//                         "
//                         '''
//                     }
//                 }
//             }
//         }
    }
}
