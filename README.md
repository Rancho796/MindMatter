## MindMatter

## Overview
MindMatter is a full-featured blogging platform designed to provide users with an intuitive interface for creating, editing, and managing blog posts. Whether you're a casual writer or a professional blogger, MindMatter makes it easy to share your stories, thoughts, and ideas with the world.

## Features
- **User Authentication**: Secure sign-up, login, and profile management.
- **Rich Text Editor**: Write and format posts with a built-in WYSIWYG editor.
- **Commenting System**: Engage readers with a user-friendly commenting feature.
- **Categories and Tags**: Organize posts for easier navigation and searchability.
- **Responsive Design**: Optimized for both desktop and mobile devices.
- **Admin Panel**: Manage users, moderate comments, and oversee content with an admin dashboard.
- **SEO-Friendly**: Built with SEO best practices to improve visibility on search engines.

## Installation
To set up MindMatter locally:

1.**Clone the repository**:
    '''bash
    git clone https://github.com/arfs-zaffar-om/Matter.git

2.**Set up a Python virtual environment**:
    '''bash
    python -m venv myenv

3.**Activate the Python Environment**:
    '''bash
    myenv\Scripts\activate

4.**Install All Dependencies Using the requirements.txt File**:
    '''bash
    pip install -r requirements.txt

5.**Change the Working Directory to src**:
    '''bash
    cd src

6.**Create a `.env` File in the `src` Folder and Add the Following Variables**:
    '''plaintext
    SECRET_KEY=
    DEBUG=
    USER=
    PASSWORD=
    PORT=
    HOST=

7.**Create Workspace and Import Collection (from the provided file)**:
    '''plaintext
    1.Click on the Import button.
    2.Select the file you previously shared that contains the collection.
    3.Once imported, go to Environments and create a new environment.
    4.In the new environment, add a variable named devurl with the appropriate development URL for your local environment.

