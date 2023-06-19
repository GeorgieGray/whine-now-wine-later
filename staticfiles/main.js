const createCheckoutSession = () => {
  return fetch(`/checkout/api/session/${window.productId}`, { method: 'POST' })
  .then(result => {
    if (!result.ok) throw new Error("Unable to create checkout session")
    
    return result.json()
  })
}

const buyNow = async (stripe) => {
  const { sessionId } = await createCheckoutSession()

  console.log('session', sessionId)
  
  stripe.redirectToCheckout({ sessionId })
}

const init = async () => {
  const { publicKey } = await fetch("/checkout/api/config")
    .then(result => {
      if (!result.ok) throw new Error("Unable to get checkout config")
      
      return result.json()
    })
    
  const stripe = Stripe(publicKey)
  
  const button = document.getElementById('buy-now')
  if (!button) throw new Error("Cannot find buy now button")
  
  button.addEventListener("click", () => buyNow(stripe))
}

init()