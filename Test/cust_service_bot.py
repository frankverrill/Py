""" cust = customer/
selected = every function where there is an option to select/
"""


def cust_service_bot():  # Automated web customer support
    print(
        "The DNS Cable Company's Service Portal.",
        "Are you a new or existing customer?",
        "\n [1] New",
        "\n [2] Existing")
    selected = input("Enter [1] or [2]: ")
    if selected == "1":
        print("new_cust()")
    elif selected == "2":
        existing_cust()
    else:
        print("Try again, select only: [1] or [2]")
        cust_service_bot()


def new_cust():  # Select type of service for New Customer
    print("How can we help?",
          "\n[1] Sign up for service?",
          "\n[2] Schedule home visit?",
          "\n[3] Speak to live person?")
    selected = input(
        "Enter [1], [2] or [3]: ")
    if selected == "1":
        sign_up()
    elif selected == "2":
        home_visit("home visit")
    elif selected == "3":
        live_rep("sales")
    else:
        print("Try again, select only: [1], [2] or [3]")
        new_cust()


def sign_up():  # New customer selects options to sign up for
    print("Please select the package ",
          "you are interested in signing up for:",
          "\n[1] Bundle (Internet + Cable)",
          "\n[2] Internet",
          "\n[3] Cable")
    selected = input("Enter [1], [2] or [3]: ")
    if selected == "1":
        print("You've selected the Bundle Package! ",
              "Schedule a home visit and our technician ",
              "will come out and set up your new service.")
        home_visit("new install")
    elif selected == "2":
        print("You've selected the Internet Only Package! ",
              "Schedule a home visit and our technician ",
              "will come out and set up your new service.")
        home_visit("new install")
    elif selected == "3":
        print("You've selected the Cable Only Package! ",
              "Schedule a home visit and our technician ",
              "will come out and set up your new service.")
        home_visit("new install")
    else:
        print("Try again, select only: [1], [2] or [3]")
        sign_up()


def existing_cust():   # Type of support for existing customer
    print("What do you need help with?",
          "\n[1] TV",
          "\n[2] Internet",
          "\n[3] Speak to a Live Person")
    selected = input("Enter [1], [2] or [3]: ")
    if selected == "1":
        tv()
    elif selected == "2":
        internet()
    elif selected == "3":
        live_rep("sales")
    else:
        print("Try again, select only: [1], [2] or [3]")
        existing_cust()


def tv():  # TV support
    print("What is the issue?",
          "\n   [1] Can't access certain channels",
          "\n   [2] Picture is blurry",
          "\n   [3] Keep losing service",
          "\n   [4] Other issues")
    selected = input("Enter [1], [2], [3] or [4]: ")
    if selected == "1":
        print("Please check the channel lists at DefinitelyNotSinister.com.:",
              "\nIf the channel you cannot access is there,",
              "\nplease contact a live representative.")
        did_that_help("a blurry picture")
    elif selected == "2":
        print("Try adjusting the antenna above your television set.")
        did_that_help("adjusting the antenna")
    elif selected == "3":
        print("Is it raining outside? If so, ",
              "\nwait until it's not raining, then try again.")
        did_that_help("the rain outside")
    elif selected == "4":
        live_rep("support")
    else:
        print("Try again, select only: [1], [2] or [3]")
        tv()


def internet():  # Internet support
    print("What is the issue?",
          "\n[1] Can't connect to internet",
          "\n[2] Very slow connection",
          "\n[3] Can't access certain sites",
          "\n[4] Other issues")
    selected = input("Enter only: [1], [2], [3] or [4]: ")
    if selected == "1":
        print("Unplug your router, then plug it back in, "
              "then give it a good whack, like the Fonz.")
        did_that_help("can't connect to internet")
    elif selected == "2":
        print("Move to a different region or install a VPN. ",
              "Some areas block certain sites")
        did_that_help("very slow connection")
    elif selected == "3":
        print("Is it raining outside? If so, ",
              "wait until it's not raining, then try again.")
        did_that_help("can't access certain sites")
    elif selected == "4":
        live_rep("support")
    else:
        print("Try again, select only: [1], [2] or [3]")
        internet()


def did_that_help(message):  # Did that support answer help?
    print(message)


def home_visit(purpose):  # Book a home visit
    print(purpose)


def live_rep(message):  # Live person support
    print(message)


cust_service_bot()  # Function call to automated customer support
