FROM python:3
EXPOSE 8000

RUN git clone https://github.com/StarodubcevDV/back_courses.git
RUN pip install --no-cache-dir -r /back_courses/requirements.txt
