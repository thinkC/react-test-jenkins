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
                sh 'C:\\Users\\M3Trainee\\AppData\\Local\\Programs\\Python\\Python311\\python3.exe test-jenkins.py'
            }
        }
    }
}