// pipeline{
//     agent any

//     stages{
//         stage("Verify Branch"){
//         steps{
//             echo "$GIT_BRANCH"
//         }
//         }
//         stage("Install Dependencies"){
//             steps{
//                 // dir("$WORKSPACE"){
//                 //     sh 'npm install'
//                 // }
//              pwsh(script: """
                
//                 npm install

                
//                 """)
//             }
//         }
//         stage("Check Node.js and npm versions"){
//             // steps{
//             //     sh 'node -v'
//             //     sh 'npm -v'
//             // }
//             steps{
//             pwsh(script:"""
//             node -v
//             npm -v
//             """)
//             }

//         }
//         stage("Run Jest Test"){
//             steps{
//                 // echo "workspace is  $WORKSPACE"
//                 // dir("$WORKSPACE"){
//                 //     sh 'npm test'
//                 // }
             
//                 pwsh(script: """
                
//                 npm test

                
//                 """)
           
//             }
//         }
//     }
// }


pipeline{
    agent any

    stages{
        stage("Verify Branch"){
        steps{
            echo "$GIT_BRANCH"
            echo "Workspace is $WORKSPACE"
        }
        }
        stage("Check Node.js and npm versions") {
    steps {
    //     dir("$WORKSPACE") {
    //     //     withEnv(["PATH+NODEJS=C:\\Program Files\\nodejs", "PATH+NPM=C:\\Program Files\\nodejs"]) {
    //     //     sh 'which node'
    //     //     sh 'which npm'
    //     //     sh 'node -v'
    //     //     sh 'npm -v'
    //     // }
    //         sh 'which node'
    //         sh 'which npm'
    //         sh 'node -v'
    //         sh 'npm -v'
    // }
    bat 'node -v'
    bat 'npm -v'
}

        stage("Install Dependencies"){
            steps{
                // dir("$WORKSPACE"){
                //     sh 'npm install'
                // }
                bat 'npm install'
            }
        }

        // stage("Check Node.js and npm versions"){
        //     steps{
        //         dir("$WORKSPACE") {
        //             sh 'node -v'
        //             sh 'npm -v'
        //         }
        //     }


        // }
        stage("Run Jest Test"){
            steps{
                echo "workspace is  $WORKSPACE"
                // dir("$WORKSPACE"){
                //     sh 'npm test'
                // }
                bat 'npm test'
            }
        }
    }
}
}