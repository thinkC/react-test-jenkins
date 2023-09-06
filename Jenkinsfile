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
                // dir("$WORKSPACE"){
                //     sh 'npm install'
                // }
             pwsh(script: """
                
                npm install

                
                """)
            }
        }
        stage("Check Node.js and npm versions"){
            // steps{
            //     sh 'node -v'
            //     sh 'npm -v'
            // }
            steps{
            pwsh(script:"""
            node -v
            npm -v
            """)
            }

        }
        stage("Run Jest Test"){
            steps{
                // echo "workspace is  $WORKSPACE"
                // dir("$WORKSPACE"){
                //     sh 'npm test'
                // }
                steps{
                pwsh(script: """
                
                npm test

                
                """)
                }

            }
        }
    }
}