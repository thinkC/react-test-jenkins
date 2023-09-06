pipeline{
    agent any

    stages{
        stage("Verify Branch"){
        steps{
            echo "$GIT_BRANCH"
        }
        }

        stage("Run Jest Test"){
            steps{
                echo "workspace is  $WORKSPACE"
                dir("$WORKSPACE/react-test-jenkins"){
                    sh '/c/Program Files/nodejs/npm test'
                }
            }
        }
    }
}