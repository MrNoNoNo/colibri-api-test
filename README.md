Colibri API

Pre-requisites:

Docker Compose and docker(implicitly) is needed to run this mini API

To build the image run:
- docker-compose build

After the image is built run:
- docker-compose up -d

Migrations have to be applied. To apply migrations, run:
- docker-compose exec web python manage.py migrate

To run the unit tests, execute the following command:
- docker-compose exec web python manage.py test

The following URLs are available:

http://localhost:8000/api/employees - lists all employees stored in the database
http://localhost:8000/api/employees/<id:1-3000> - lists an employee details

http://localhost:8000/api/average/age/industry - displays statistics about average ages per industry
http://localhost:8000/api/highest/age/industry - displays statistics about highest ages per industry
http://localhost:8000/api/lowest/age/industry - displays statistics about lowest ages per industry

http://localhost:8000/api/average/salaries/experience - displays statistics about average salaries per years of experience
http://localhost:8000/api/highest/salaries/experience - displays statistics about highest salaries per years of experience
http://localhost:8000/api/lowest/salaries/experience - displays statistics about lowest salaries per years of experience

http://localhost:8000/api/average/salaries/industry - displays statistics about average salaries per industry
http://localhost:8000/api/highest/salaries/industry - displays statistics about highest salaries per industry
http://localhost:8000/api/lowest/salaries/industry - displays statistics about lowest salaries per industry

http://localhost:8000/api/average/salaries/gender - displays statistics about average salaries per gender
http://localhost:8000/api/highest/salaries/gender - displays statistics about highest salaries per gender
http://localhost:8000/api/lowest/salaries/gender - displays statistics about lowest salaries per gender
