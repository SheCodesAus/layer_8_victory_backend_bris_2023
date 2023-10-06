# Instructions For Setting Up This Repo

## FIRST, One Person In The Group Should:
1. Clone this repo down using `git clone insert_quick_setup_link_here`
2. Create and activate a `venv` as normal
3. Run `pip install -r requirements.txt` to install dependencies
4. Create a Django project with `django-admin startproject <your_app_name>`
5. Check you're happy with the files to stage, using `git status` 
6. Stage each file in turn with `git add <filename_here>`
7. Create the initial commit with `git commit -m "initial commit"`
8. Push to origin/main, using `git push origin main`

## THEN, All Other Group Members Should:
1. Clone the repo down with `git clone insert_quick_setup_link_here`
2. Create and activate a `venv`
3. Install dependencies with `pip install -r requirements.txt`

## Finally:
1. One group member should make a push replacing this readme text with the skeleton of your readme document.
2. All other group members should pull down this change (`git pull origin main`)

> For next steps, take a look back at the "Project Setup" lesson in the DRF content.
>
> Try and get the most minimal possible app deployed ASAP, using the DRF "Deployment" lesson. Even just an endpoint that only returns "Hello world" is a good way to start. Only one person needs to get the deployment set up, and after that other people should be able to merge feature branches into `main` as described on the Thinkific notes.