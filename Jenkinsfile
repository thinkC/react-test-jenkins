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
    }
}