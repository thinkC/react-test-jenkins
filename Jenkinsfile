pipeline{
    agent any
    stages{
        stage("Verify Branch"){
        steps{
            echo "$GIT_BRANCH"
            echo "Workspace is $WORKSPACE"
        }
        }
        stage{
            steps{
                sh 'python test-jenkins.py'
            }
        }
    }
}