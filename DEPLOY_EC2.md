# AWS EC2 Deployment Instructions for Flask App

1. **Launch an EC2 Instance**
   - Use an Ubuntu Server AMI (e.g., Ubuntu 22.04 LTS).
   - Allow inbound traffic on port 22 (SSH) and 5000 (Flask) or 80 (for production).

2. **Connect to your EC2 Instance**
   - Use SSH: `ssh -i <your-key.pem> ubuntu@<ec2-public-dns>`

3. **Install Docker**
   - `sudo apt update`
   - `sudo apt install -y docker.io`
   - `sudo systemctl start docker`
   - `sudo systemctl enable docker`

4. **Clone or Upload Your Project**
   - Use `git clone` or SFTP to upload your project files to the EC2 instance.

5. **Build and Run the Docker Container**
   - `cd <your-project-directory>`
   - `sudo docker build -t flask-app .`
   - `sudo docker run -d -p 80:5000 flask-app`

6. **Access Your App**
   - Visit `http://<ec2-public-dns>/` in your browser.

7. **(Optional) Set Up a Reverse Proxy (Nginx)**
   - For production, use Nginx to proxy requests to your Flask app.

8. **(Optional) Set Up HTTPS**
   - Use Certbot with Nginx for SSL certificates.

---

**Note:** Ensure your `model.pkl` and `Web_Performance.csv` are present in the project directory.
