# Docker_Assignment
I have created a Python Project using flask:</br>
![Screenshot 2025-05-12 124410](https://github.com/user-attachments/assets/c422de3b-558e-460e-86ae-c0a24af7588b)

TL;DR : vim main.py wrote a python flask</br>
<pre>
  from flask import Flask

  app = Flask(__name__)

  @app.route('/')
  def hello_surya():
      return "<h-1>Hello Surya!</h-1>"

  if __name__ == '__main__':
      app.run(host="0.0.0.0", port=5000, debug=True)

</pre></br>
![Screenshot 2025-05-12 124418](https://github.com/user-attachments/assets/82eda6f8-9de7-47ca-94dc-b9f1eb549809)</br>
In my LocalDevice it working as you can see in the picture:</br>
![Screenshot 2025-05-12 124545](https://github.com/user-attachments/assets/0bf469ab-4f43-4f14-951c-4391826650b5)</br>
</br>
As i need this project to share to sai, i need to create Dockerfile and share it.</br>
![image](https://github.com/user-attachments/assets/2f7925ce-53c9-4faa-9e7b-8b0684726d7e)
</br>
![image](https://github.com/user-attachments/assets/8e8c0ecd-bbe3-4f59-9c54-efb155ef3daf)
</br>
Now Build the docker</br>
<pre>docker build -t suryatopsasmal/myimage</pre></br>
##-t is tage</pre>
now Push it to Docker registry</br>
<pre>docker push suryatopsasmal/myimage</pre></br>
--------------------------------------------------------------------------------------------------------------------</br>

now sai has to pull the image</br>
<pre>docker pull suryatopsasmal/myimage</pre>
</br>
after pulling.... the image run it....
</br>
<pre>docker run --rm -p 5000:5000 suryatopsasmal/myimage</pre>
</br>
in the brouser in search bar:</br>
<pre>localhost:5000</pre>
</br>
You will see: </br>
<img src="https://github.com/user-attachments/assets/411bf842-28a3-4f46-bc30-4459ff003a7c">











