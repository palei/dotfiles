# My dotfiles

Configs and other files I like having on all my systems.

## Install

Clone this repo:

    git clone git@github.com:palei/dotfiles.git

Install requirements:

    pip install -r requirements.txt

Install the files like so:

    cd dotfiles
    ./install

The installation script creates a symlink for everything defined in the `settings.yaml` file. It will not replace existing files, but will update existing symlinks. This means you'll have to manually delete (or move) files like .bashrc if you want to install the one from this repository.

## Adjusting to your needs

Fork the repository, delete things you don't need and add your own stuff!
