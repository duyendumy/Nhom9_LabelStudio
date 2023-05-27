## Test Label Studio

Label Studio is an open source data labeling tool. It lets you label data types like audio, text, images, videos, and time series with a simple and straightforward UI and export to various model formats. It can be used to prepare raw data or improve existing training data to get more accurate ML models.

This project is used for testing the Label Studio application. Group 9 use Selenium to test the basic functionalities and use Allure to generate reports.

Software Requirement Specification [Docs](https://docs.google.com/document/d/1wH-JTws-e2QWNwUOfaP1agbtjZV4rkDm1Rp0unthgeo/edit?usp=sharing)

#### Install locally with Docker

Group 09 Label Studio docker image is [here](https://hub.docker.com/repository/docker/duyendu/group_09_label_studio).

```bash
# You can pull this docker repository
docker pull duyendu/group_09_label_studio

# Run this image after install
docker run -it -p 8080:8080 duyendu/group_09_label_studio
```

#### Build a local image with Docker

```bash
# Download zip or git clone source code
pip clone "https://github.com/duyendumy/Nhom9_LabelStudio.git"

# To Build a local image, run:
docker build -t yourusername/label-studio:latest .
```

#### Deploy in a cloud instance

We deploy this app to AWS Academy using Elastic Beanstalk service.
This is domain [here](http://testlabelstudio.us-east-1.elasticbeanstalk.com/)

If you want to deploy by docker, please follow this detailed instructions [docs](https://docs.google.com/document/d/1fw_0v-iWkRd5rYkOMR-NFacxEHoJWz-W/edit?usp=sharing&ouid=100172530492298207195&rtpof=true&sd=true)

#### Run test selenium

```bash
# Install dependencies
pip install -r requirements.txt
pip install -r deploy/requirements.txt
pip install -r deploy/requirements-test.txt
cd label_studio

# To run all test selenium, run:
pytest -v -s test_selenium --alluredir=allure_reports

# To run specific test functionality
pytest -v -s test_selenium/test_createproject.py --alluredir=allure_reports

# To run specific test case
pytest -v -s test_selenium/test_createproject.py::TestCreateProject::test_create_valid_project --alluredir=allure_reports

# To see allure report, run:
allure serve allure_reports
```
