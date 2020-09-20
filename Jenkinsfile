 pipeline {
        environment {
            sonarkey = "${sonarkey}"
            sonarurl = "${sonarurl}"
            devurl = "${devurl}"
            sonarpath = "${sonarpath}"
        }
        agent any

        stages {
            stage('Carregando o ENV de desenvolvimento') {
                steps {
                    configFileProvider([configFile(fileId: 'f5d2e0c0-aa51-4de8-861e-3f81d3557b33', variable: 'env')]) {
                        sh 'cat $env > .env'
                    }
                }
            }

            stage('Executando o sonarqube') {
                steps {
                    sh  sonarpath + ' -Dsonar.projectKey=atap -Dsonar.sources=. -Dsonar.host.url='+ sonarurl + ' -Dsonar.login=' + sonarkey
                }
            }

            stage('Derrubando os containers antigos') {
                steps {
                    script {
                        try {
                            sh 'docker-compose down'
                        } catch (Exception e) {
                            sh "echo $e"
                        }
                    }
                }
            }        
            stage('Subindo o ambiente de dev novo') {
                steps {
                    script {
                        try {
                            sh 'docker-compose --env-file=.env up -d --build'
                        } catch (Exception e) {
                            slackSend (color: 'error', message: "[ FALHA ] Não foi possivel subir o ambiente de dev - ${BUILD_URL} em ${currentBuild.duration}s", tokenCredentialId: 'slack-token-atap')
                            sh "echo $e"
                            currentBuild.result = 'ABORTED'
                            error('Erro')
                        }
                    }
                }
            }
            stage('Notificando o slack') {
                steps {
                    slackSend (color: 'good', message: '[ Sucesso ] O novo build esta disponivel em:' + devurl, tokenCredentialId: 'slack-token-atap')
                }
            }
        }
    }