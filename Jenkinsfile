pipeline{
    agent any

    stages{
        stage("Verify Branch"){
        steps{
            echo "$GIT_BRANCH"
        }
        }
        stage("Install Dependencies"){
            steps{
                dir("$WORKSPACE/react-test-jenkins"){
                    sh 'npm install'
                }
            }
        }
        stage("Check Node.js and npm versions"){
            steps{
                sh 'node -v'
                sh 'npm -v'
            }
        }
        stage("Run Jest Test"){
            steps{
                echo "workspace is  $WORKSPACE"
                dir("$WORKSPACE\\react-test-jenkins"){
                    sh 'npm test'
                }
                // pwsh(script: """
                
                // npm test

                
                // """)
            }
        }
    }
}