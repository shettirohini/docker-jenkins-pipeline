pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'docker-jenkins-pipeline:latest'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/shettirohini/docker-jenkins-pipeline.git' 
            }
        }
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', 
                                                  usernameVariable: 'DOCKER_USER', 
                                                  passwordVariable: 'DOCKER_PASS')]) {
                    sh "docker login -u $DOCKER_USER -p $DOCKER_PASS"
                    sh "docker tag ${DOCKER_IMAGE} rohinipattanshetti/${DOCKER_IMAGE}"
                    sh "docker push rohinipattanshetti/${DOCKER_IMAGE}"
                }
            }
        }
        stage('Deploy Docker Container') {
            steps {
                sh "docker run -d -p 6000:6000 ${DOCKER_IMAGE}"
            }
        }
    }
}

