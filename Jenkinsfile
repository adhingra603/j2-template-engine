@Library('jenkins-pipeline-shared@create-repo-if-no-exist') _

pipeline {
  agent { label 'generic' }
  environment {
    REGISTRY = '678467581510.dkr.ecr.us-east-1.amazonaws.com'
    APP_NAME = 'cainc/paas-j2-template-engine'
    IMG_NAME = "${REGISTRY}/${APP_NAME}"
  }
  options {
    ansiColor colorMapName: 'XTerm'
  }
  stages {
    stage('Checkout') {
      steps {
        checkout ([$class: 'GitSCM',
          branches: [[name: "main" ]],
          userRemoteConfigs: [[
            credentialsId: 'github-enterprise',
            url: 'git@github.cainc.com:devops/j2-template-engine.git'
          ]]
        ])
      }
    }
    stage('Build') {
      steps {
        ecrBuild("${IMG_NAME}")
      }
    }
    stage('Publish') {
      steps {
        script {
        // Create a tag and store it for publishing
        // TODO: Check with Aaron; this is returning '.' instead of a valid tag
        // def SEM_TAG = semTagging()
        def SEM_TAG = 'v.1.0'
        ecrTagAndPush("${REGISTRY}", "${IMG_NAME}", "${SEM_TAG}")
        }
      }
    }
  }
}