pipeline{
    agent any
        tools {
        nodejs "NodeJS 18.17.0" // Use the name you specified
        npm "npm 9.6.7" // Specify the npm version
    }
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
                sh 'npm install'  
                sh 'npm test'    
            }
        }
    }
}