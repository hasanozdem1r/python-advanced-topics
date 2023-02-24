pipeline {
    agent any

    options {
        skipDefaultCheckout()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Pyenv') {
            steps {
                sh 'curl https://pyenv.run | bash'
            }
        }

        stage('Build') {
            when {
                branch 'master'
            }

            environment {
                PYTHON_VERSION = '3.9'
            }

            steps {
                sh "eval '$(pyenv init -)'"
                sh "pyenv install -s ${PYTHON_VERSION}"
                sh "pyenv local ${PYTHON_VERSION}"
                sh "export PYTHONPATH=$PWD"
                sh "curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -"
                sh "source $HOME/.poetry/env"
                sh "poetry config virtualenvs.in-project true"
                sh "poetry install"
            }

            post {
                always {
                    stash name: 'venv', includes: '.venv'
                }
                success {
                    // Cache the virtual environment and dependencies
                    cache(key: "${PYTHON_VERSION}", paths: ['.venv'])
                    cache(key: "${PYTHON_VERSION}-deps", paths: ['poetry.lock'])
                }
            }
        }
    }
}
