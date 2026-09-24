pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
               
                echo 'Checking out source code...'
            }
        }

        stage('Generate Report') {
            steps {
                
                echo "BUILD_NUMBER: ${env.BUILD_NUMBER}"
                echo "JOB_NAME: ${env.JOB_NAME}"
                echo "WORKSPACE: ${env.WORKSPACE}"

                
            }
        }

        stage('Archive Report') {
            steps {
               
                archiveArtifacts artifacts: 'build_report.txt', fingerprint: true
            }
        }
    }
}
