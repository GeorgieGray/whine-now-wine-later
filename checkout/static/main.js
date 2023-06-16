fetch("/checkout/config")
    .then(result => result.json())
    .then(({ publicKey }) => {
        const stripe = Stripe(publicKey)

        window._stripe = stripe
    })