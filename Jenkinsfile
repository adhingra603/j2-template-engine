pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Building the project..."'
                // Insert your build commands here
            }
        }

        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
                // Insert your test commands here
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Deploying the application..."'
                // Insert your deployment commands here
            }
        }
    }
}
