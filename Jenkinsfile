pipeline{
    agent any
    stages{
        stage("Verify Branch"){
        steps{
            echo "$GIT_BRANCH"
            echo "Workspace is $WORKSPACE"
        }
        }
        stage("Run python script"){
            steps{
                sh 'python3 test-jenkins.py'
            }
        }
        stage("Run npm commands") {
            steps {
                sh '/home/ubuntu/.nvm/versions/node/v18.17.0/bin/node/npm install'  // Replace "/path/to/npm" with the actual path to npm
                sh '/home/ubuntu/.nvm/versions/node/v18.17.0/bin/npm/npm test'     // Replace "/path/to/npm" with the actual path to npm
            }
        }
    }
}