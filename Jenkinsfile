pipeline {
    agent { label 'build'}

    triggers {
        githubPush() 
    }

    stages {
        stage('Checkout') {
            steps {
                // checkout scm
                dir('simple-api') {
                    git credentialsId: 'muyumq-github', url: 'https://github.com/CE-SPDX-The-Best/simple-api-best.git', branch: 'main'
                }

                dir('simple-api-robot') {
                    git credentialsId: 'muyumq-github', url: 'https://github.com/CE-SPDX-The-Best/simple-api-best-robot.git', branch: 'main'
                }
            }
        }

        stage('Setup Environment (simple-api)') {
            steps {
                dir('simple-api') {
                    echo "1. Creating Python virtual environment (venv)..."
                    // สร้างโฟลเดอร์ venv
                    sh 'python3 -m venv venv' 

                    echo "2. Activating venv and installing requirements..."
                    // รันคำสั่งใน shell session เดียว
                    // 'source' จะ activate venv
                    // 'pip install' จะติดตั้งลงใน venv นั้นทันที
                    sh '''
                    . venv/bin/activate
                    pip install -r requirements.txt
                    echo "--- Packages installed in venv: ---"
                    pip list
                    '''
                }
            }
        }

        stage('Setup Environment (simple-api-robot)') {
            steps {
                dir('simple-api-robot') {
                    sh 'python3 -m venv venv' 
                    sh '''
                       . venv/bin/activate
                       pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Unittests') {
            steps {
                dir('simple-api') {
                    sh '''
                    . venv/bin/activate
                    python -m unittest unit_test.py
                    '''
                }
            }
        }
        
        stage('Build-Run simple-api') {
            steps {
                dir('simple-api') {
                    sh 'docker compose up -d --build'
                    sh 'sleep 5'
                }
            }
        }

        stage('Run Robot Framework Tests') {
            steps {
                dir('simple-api-robot') {
                    sh '''
                       . venv/bin/activate
                       echo "--- Using Robot from: $(which robot) ---"
                       robot robot-test.robot 
                    '''
                }
            }
            // 'post' จะทำงานเสมอหลัง 'steps'
            post {
                always {
                    // !!! สำคัญ: ต้องกลับไปที่ 'simple-api' เพื่อสั่ง 'down'
                    dir('simple-api') {
                        echo "Stopping docker-compose services..."
                        sh 'docker compose down'
                    }
                }
            }
        }

        stage('Push to GHCR') {
            steps {
                    withCredentials([usernamePassword(credentialsId: 'muyumq-github', usernameVariable: 'GHCR_USER', passwordVariable: 'GHCR_PAT')]) {
                        sh "echo ${GHCR_PAT} | docker login ghcr.io -u ${GHCR_USER} --password-stdin"
                        sh "docker tag simple-api:latest ghcr.io/ce-spdx-the-best/simple-api:latest"
                        sh "docker push ghcr.io/ce-spdx-the-best/simple-api:latest"
                    }
            }
        }

        stage('Deploy to Production (VM3)') {
            steps {
                sshagent(credentials: ['ssh-key']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no admin@192.168.56.106 '
                        docker pull ghcr.io/ce-spdx-the-best/simple-api:latest
                        docker stop production-api || true
                        docker rm production-api || true
                        docker run -d --name production-api -p 5000:5000 ghcr.io/ce-spdx-the-best/simple-api:latest
                    '
                    """
                }
            }
        }
    }

    post {
        always {
            // ทำความสะอาด venv ทั้ง 2 ที่
            echo "Cleaning up virtual environments..."
            sh "rm -rf simple-api/venv"
            sh "rm -rf simple-api-robot/venv"
            
            sh "docker logout ghcr.io || true"
        }
    }
}