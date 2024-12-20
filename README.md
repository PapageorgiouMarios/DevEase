# DevEase: Simplify Your Workflow 👨🏻‍💻

Dear developers,

Have you ever wondered how many repetitive actions you perform every time you open your laptop or desktop to start your work? 

Most of us, even non-developers, open the same tools and websites by double-clicking application icons or launching a browser to visit specific sites.

What if I told you it’s possible to automate these actions—and more—by simply pressing a number?

This is where **DevEase** takes action! 🚀

![DevEase Logo](https://github.com/user-attachments/assets/585599ba-284d-4b79-a6ab-804272ae101d)

DevEase is a versatile multi-tool that works on both **Linux** 🐧 and **Windows**. By selecting specific numbers, the program can perform multiple actions. Here's a brief overview:

---

## Features

### 1. **Open Tool**
Opens `.exe` files for specific programs on your device—think of it as an equivalent to double-clicking an application icon.

![Open Tool Example](https://github.com/user-attachments/assets/b54cbcbd-7050-47ba-9a7a-7806c9526e34)

---

### 2. **Open Website**
Launches a website using its URL, much like typing the address in your default browser.

![Open Website Example](https://github.com/user-attachments/assets/2944bf42-e01a-40a3-8a17-5a16d2565b44)

---

### 3. **Empty Recycle Bin**
Empties your device’s Recycle Bin or Trash. Many users forget to permanently delete files, and this feature helps keep storage organized.

![Empty Recycle Bin Example](https://github.com/user-attachments/assets/4bf5a9fe-c75e-47f5-9de6-314947b0d8bf)

---

### 4. **Review Device**
Displays detailed information about your device's hardware—no need for terminals or long commands! This includes:

1. **OS**: Operating system details (name, version, release, etc.).
2. **RAM**: Total capacity, used memory in GB, and usage percentage.
3. **Disk**: Storage capacity, used space in GB, and percentage.
4. **Network**: Interfaces (IP, Netmask, Gateway).
5. **Antivirus Status**: Lists installed antivirus software and their states (Enabled/Disabled).
6. **Wi-Fi Credentials**: Saved networks and passwords (convenient for finding forgotten credentials).
7. **Location**: Displays your approximate location based on your public IP (via the `ipify` API).
   > ⚠️ *Warning*: Do not share your public IP address with anyone. The displayed location corresponds to your ISP, not your exact address.
8. **CPU**: Processor details, number of cores, and maximum clock speed.
9. **GPU**: Graphics card details (adapter, version).
10. **Wi-Fi Config**: Adapter info, available networks, and hosted network details.
11. **Chipset**: Manufacturer, product, serial number, and version.
12. **Environment Variables**: Lists all environment variables and their file locations.

![Device Review Example](https://github.com/user-attachments/assets/f7fe86f5-a72b-4f69-a930-e10e1c0a2016)

---

## Development

This project was built using **Python** 3.11 🐍 in **Visual Studio Code** 💻.

---

## Docker Integration 🐳

To test DevEase on Docker, follow these steps:

1. **Install Docker**:  
   You can install the Docker extension directly in **Visual Studio Code**.  

2. **Create a Dockerfile**:  
   Include all the necessary information to run the program. Ensure your project is inside a dedicated folder so Docker knows the working directory.

3. **Check Python Version**:  
   Run the following command to confirm your Python version:
   ```bash
   python --version

4. **Generate `requirements.txt`**
When creating your project, you might use third-party packages. To ensure Docker installs all dependencies, create a `requirements.txt` file by running:
   ```bash
   pip freeze > requirements.txt  

5. **Build and Run the Docker Container**

After preparing your `Dockerfile` and project folder, follow these steps:

- **Build the Docker Image**:  
  Run the following command to build your Docker image:
   ```bash
   docker build -t IMAGE NAME .

 - **Run the Docker Image**:
   Finally, to run Devease simply run:
   ```bash
   docker run -it IMAGE NAME

