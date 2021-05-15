#!/usr/bin/env python3
# -*- coding: utf-8 -*-

ogprompt = """
Operating system: Arch Linux

Input: Print the current directory
Output: pwd
###
Input: List files
Output: ls -l
###
Input: Change directory to /tmp
Output: cd /tmp
###
Input: Count files
Output: ls -l | wc -l
###
Input: Replace foo with bar in all python files
Output: sed -i .bak -- 's/foo/bar/g' *.py
###
Input: Push to master
Output: git push origin master
###
"""

template = """
Input: {}
Output:
"""

import os, click, openai

while True:
    request = input(click.style('nlsh> ', 'red', bold=True))
    prompt = ogprompt.rstrip() + template.format(request)

    result = openai.Completion.create(
        engine='davinci', prompt=prompt.strip(), stop="###", max_tokens=100, temperature=.0
    )

    command = result.choices[0]['text'].strip()
    prompt = prompt.strip() + " " + command + "\n###\n"

    print(command)