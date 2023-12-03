#!/bin/bash

while true; do
    # Display menu options
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"
    
    # Request user input
    read -p "Enter your choice (1-4): " choice

    # Evaluate user input
    case $choice in
        1)
            # Option 1: Hello world
            echo "Hello world!"
            ;;
        2)
            # Option 2: Ping self
            ping -c 4 127.0.0.1
            ;;
        3)
            # Option 3: IP info
            ifconfig
            ;;
        4)
            # Option 4: Exit
            echo "Exiting program. Goodbye!"
            exit 0
            ;;
        *)
            # Invalid choice
            echo "Invalid choice. Please enter a number between 1 and 4."
            ;;
    esac

    # Add a newline for better readability
    echo

done
