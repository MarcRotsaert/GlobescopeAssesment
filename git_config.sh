#!/usr/bin/env bash

argument_names=("name" "email")
argument_values=("$@")
nr_of_arguments=${#argument_values[@]}

if [ $nr_of_arguments -lt ${#argument_names[@]} ]; then
    printf "USAGE: %s %s\n" "$0" "${argument_names[*]}"
    exit 1;
fi

gitUser="${argument_values[0]}"
gitEmail="${argument_values[1]}"
repoURL="git@github.com:${gitUser}/GlobescopeAssesment.git"

echo "Initialize git"
git init

echo "Stage README.md"
git add README.md

printf "Configure with username %s and email %s\n" ${gitUser} ${gitEmail}
git config user.name ${gitUser}
git config user.email ${gitEmail}

echo "Disable rebase pull policy"
git config pull.rebase false

echo "Create main branch"
git branch -M main

printf "Add upstream %s\n" ${repoURL}
git remote add origin ${repoURL}