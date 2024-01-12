import streamlit as st

st.set_page_config(page_title="Information Section", page_icon="ℹ️", layout="wide")

st.title("Dark Pattern Categories")

st.subheader("Sneaking")
st.info(
    "Attempting to misrepresent user actions, or delay information that if made available to users, they would likely object to.")
with st.expander(
        "Examples of Sneaking"):
    st.markdown(
        """
        ##### 1. Sneak into Basket
        Adding additional products to users' shopping carts without their consent.
        """
    )
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/sb-1.png",
             caption="Sneak into Basket on avasflowers.net. Despite requesting no greeting cards, one worth $3.99 is included.")
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/sb-5.png",
             caption="Sneak into Basket on cellularoutfitter.com. The pre-checked box means the screen protector worth $4.99 ends up in cart.")

    st.markdown(
        """
        ##### 2. Hidden Costs
        Revealing previously undisclosed charges to users right before they make a purchase.
        """
    )
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/sb-2.png",
             caption="Hidden Costs on proflowers.com. The Care & Handling charge ($2.99) is disclosed on the last step.")

    st.markdown(
        """
        ##### 3\. Hidden Subscription
        Charging users a recurring fee under the pretense of a one-time fee or a free trial.
        
        Prevalence: 14 instances across 13 websites.
        
        """
    )
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/hs-1.png",
             caption="Hidden Subscription on wsjwine.com. Selecting the WSJwine Advantage option does not reveal the recurring subscription of $89 unless \"Learn More\" is clicked on.")
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/hs-3.png",
             caption="Hidden Subscription on ross-simons.com. Joining the VIP Rewards Club does not reveal the recurring subscription of $95 unless \"Terms and conditions\" is clicked on.")

st.subheader("Urgency")
st.info("Imposing a deadline on a sale or deal, thereby accelerating user decision-making and purchases.")
with st.expander(
        "Examples of Urgency"):
    st.markdown(
        """
        ##### 1. Countdown Timer
        Indicating to users that a deal or discount will expire using a counting-down timer.
        """
    )
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/urgency-1.png",
             caption="Countdown Timer on justfab.com. In this instance, the stated offer is valid even after the hour long timer expires.")
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/urgency-2.png",
             caption="Countdown Timer in a popup displayed on leesa.com. In this instance, the stated offer is valid even after the half hour long timer expires.")

    st.markdown(
        """
        ##### 2. Limited-time Message
        Indicating to users that a deal or sale will expire will expire soon without specifying a deadline, thus creating uncertainty.
        """
    )
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/urgency-4.png",
             caption="Limited Time on samsung.com. The website states that the deal is \"Limited Time Only\" without disclosing the deal's deadline.")

st.subheader("Misdirection")
st.info("Using visuals, language, or emotion to steer users toward or away from making a particular choice.")
with st.expander(
        "Examples of Misdirection"):
    st.markdown(
        """
        ##### 1. Confirmshaming
        Using language and emotion (shame) to steer users away from making a certain choice.
        """
    )
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/cs-1.png",
             caption="Confirmshaming on radioshack.com. The option to dismiss the popup is framed to shame the user into avoiding it.")

    st.markdown(
        """
        ##### 2. Visual Interference
        Using style and visual presentation to steer users to or away from certain choices.
        """
    )
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/vi-1.png",
             caption="Visual Interference on greenfingers.com. The opt-out option is grayed out to indicate it is disabled or cannot be clicked, when it can.")

    st.markdown(
        """
        ##### 3. Trick Questions
        Using confusing language to steer users into making certain choices.
        """
    )
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/tq-1.png",
             caption="Trick Questions on newbalance.co.uk. Normally, checkboxes are designed to be ticked to opt in. In this case however, the user is required to tick to opt out.")

    st.markdown(
        """
        ##### 4. Pressured Selling
        Pre-selecting more expensive variations of a product, or pressuring the user to accept the more expensive variations of a product and related products.
        """
    )
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/ps-1.png",
             caption="Pressured Selling on topcoat.store. On adding a product to cart, a popup appears asking the user to upgrade their purchase.")

st.subheader("Social proof")
st.info("Influencing users' behavior by describing the experiences and behavior of other users.")
with st.expander(
        "Examples of Social proof"):
    st.markdown(
        """
        ##### 1. Activity Messages
        Informing the user about the activity on the website (e.g., purchases, views, visits).
        """
    )
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/sp-2.png",
             caption="Activity Notification on thredup.com highlighting the names and locations of those who purchased the product. The message always signals sold products as \"just saved\" by customers even though the products have been sold for a long time.")
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/sp-1.png",
             caption="Activity Notification on jcpenney.com highlighting the number of people who viewed the product in the last day.")

    st.markdown(
        """
        ##### 2. Testimonials of Uncertain Origin
        Testimonials on a product page whose origin is unclear.
        """
    )
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/testimonial.png",
             caption="Testimonials on spanx.com. The website does not disclose how these were sourced, or whether they were submitted by actual customers.")

st.subheader("Scarcity")
st.info("Signaling that a product is likely to become unavailable, thereby increasing its desirability to users.")
with st.expander(
        "Examples of Scarcity"):
    st.markdown(
        """
        ##### 1. Low-stock Message
        Indicating to users that limited quantities of a product are available, increasing its desirability.
        """
    )
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/s-1.png",
             caption="Low-stock Message on 6pm.com. Choosing product options shows _Only 3 left in stock_. The out-of-stock message makes it always seem that the item just sold out.")
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/ls-2.png",
             caption="Low-stock Message on orthofeet.com. The message does not disclose the quantity in stock to users and appears for all products on the website.")

    st.markdown(
        """
        ##### 2\. High-demand Message
        Indicating to users that a product is in high-demand and likely to sell out soon, increasing its desirability
        
        Prevalence: 47 instances across 43 websites.
        
        """
    )
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/hd-1.png",
             caption="High Demand on fashionnova.com. The message is shown for all products on the website.")
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/hd-2.png",
             caption="High Demand on pacificcoast.com. The message is shown for all products on the website.")

st.subheader("Obstruction")
st.info("Making it easy for the user to get into one situation but hard to get out of it.")
with st.expander(
        "Examples of Obstruction"):
    st.markdown(
        """
        ##### 1. Hard to Cancel
        Making it easy for the user to sign up for a recurring subscription but cancellation requires emailing or calling customer care.
        """
    )
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/o1.png",
             caption="Hard to Cancel on savagex.com. The only way to cancel the $49.95 auto-renewing membership is to call the customer support. Signing up, on the other hand, can be completed online.")
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/o3.png",
             caption="Hard to Cancel on 1800flowers.com. The only way to cancel the $19.99 auto-renewing membership is to email customer care unlike signing up, which can be completed online.")

st.subheader("Forced Action")
st.info("Forcing the user to do something tangential in order to complete their task.")
with st.expander(
        "Examples of Forced Action"):
    st.markdown(
        """
        ##### 1. Forced Enrollment
        Coercing users to create accounts or share their information to complete their tasks.
        """
    )
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/fa-1.png",
             caption="Forced Action on therealreal.com. Even viewing products requires signing up and creating and account.")

    st.markdown(
        """
        ##### 2. Forced Consent
        Coercing users to consent to sharing their information to complete their tasks.
        """
    )
    st.image("https://webtransparency.cs.princeton.edu/dark-patterns/assets/images/fa-2.png",
             caption="Forced Consent on theguardian.com. The website requires users to consent to sharing their information to continue using the website.")

hide_streamlit_style = """
                    <style>
                    # MainMenu{
                        visibility: hidden;
                    }
                    footer {
                        visibility: hidden;
                    }
                    footer:after {
                        content:'Developed by PerryThePlatypus Team'; 
                        visibility: visible;
                        display: block;
                        position: relative;
                        # background-color: red;
                        padding: 15px;
                        top: 2px;
    	            }
    	            img{
                        border-radius: 10px !important;
                    }
                    </style>
                    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
