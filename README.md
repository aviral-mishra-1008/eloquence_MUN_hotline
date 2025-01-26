# Hotline - MUN Communication Platform for Eloquence

Hotline is a dedicated communication platform designed for MUN under Eloquence, the annual Model United Nations conference organized by the Literary Club of Motilal Nehru National Institute of Technology (MNNIT), Allahabad. This platform facilitates secure and organized diplomatic communications between participating nations during the conference.

## Features

### For Delegates
- **Secure Login System**: Each delegate receives unique credentials representing their assigned nation
- **Nation-to-Nation Communication**: Direct messaging system between participating countries
- **Executive Board Communication**: Direct channel to communicate with the Executive Board
- **Real-time Notifications**: Instant notifications for new messages
- **Message History**: Complete record of all diplomatic communications
- **National Flag Display**: Visual representation of each nation through their flags

### For Executive Board (Admin)
- **User Management**: Create and manage delegate accounts
- **Broadcast Capabilities**: Send messages to all participants
- **Message Monitoring**: Overview of diplomatic communications
- **Access Control**: Manage participant permissions and access

## Technical Stack
- **Backend**: Django
- **Frontend**: Tailwind CSS, HTML and Javascript
- **Database**: SQLite3
- **Authentication**: Django's built-in authentication system
- **File Handling**: Pillow for flag images

## Installation & Setup

### Clone the repository
```bash
git clone https://github.com/aviral-mishra-1008/eloquence_MUN_hotline.git
cd eloquence_MUN_hotline
```

### Install requirements
```bash
pip install -r requirements.txt
```

### Run migrations
```bash
python manage.py migrate
```

### Create superuser (for Executive Board access)
```bash
python manage.py createsuperuser
```

### Run the development server
```bash
python manage.py runserver
```

## Usage
## For Administrators
- **Access the admin panel at /admin**
- **Create user accounts for delegates**
- **Assign countries and upload respective flags**
- **Manage user permissions and access**

## For Delegates
- **Login with provided credentials**
- **View assigned country and flag**
- **Send messages to other nations or EB**
- **Check notifications for new messages**
- **Access official documents through provided links**

## Contributing
For major changes, please open an issue first to discuss what you would like to change.

## About Literary Club, MNNIT
The Literary Club of MNNIT Allahabad is an official club under SAC, MNNIT dedicated to fostering literary and diplomatic skills among students. 
Eloquence, our annual fest, features various events including the Model United Nations conference, providing a platform for students to engage in diplomatic discourse and global problem-solving.

## Deployment
The hotline is live at : https://eloquencemun.pythonanywhere.com/
