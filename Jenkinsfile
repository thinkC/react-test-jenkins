pipeline{
    agent any
    //     tools {
    //     // nodejs "NodeJS 18.17.0" // Use the name you specified
    //     // npm "npm 9.6.7" // Specify the npm version
    // }
    stages{
        stage("Verify Branch"){
        steps{
            echo "$GIT_BRANCH"
            echo "Workspace is $WORKSPACE"
        }
        }
        stage("Run python script"){
            steps{
                sh 'C:\\Users\\M3Trainee\\AppData\\Local\\Programs\\Python\\Python311\\python.exe python3 test-jenkins.py'
            }
        }
        stage("Run npm commands") {
            steps {
                sh 'C:\\Program Files\\nodejs npm install'  
                sh 'C:\\Program Files\\nodejs npm test'    
            }
        }
    }
}