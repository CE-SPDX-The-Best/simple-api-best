pipeline {
    agent any
    triggers {
        pollSCM('* * * *') // Poll every 1 minutes; adjust as needed
    }
    stages {
        stage('Checkout') {
            steps {
                // Clone or pull the latest code
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sshagent (credentials: ['ssh-key']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no admin@192.168.1.56 "
                    # ไปที่ home directory
                    cd ~
                    
                    # ถ้าไม่มี repo ก็ clone ถ้ามีก็ pull อัปเดต
                    if [ ! -d simple-api ]; then
                        git clone https://github.com/CE-SPDX-The-Best/simple-api-best.git simple-api
                    else
                        cd simple-api
                        git pull origin main
                        cd ..
                    fi
                    
                    # เข้าไปที่ project
                    cd simple-api
                    
                    # สร้าง/อัปเดต image และ start service
                    docker compose up -d --build
                    "
                    '''
                }
            }
        }
    }
}
