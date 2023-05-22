// Define our component
const ReactApp = () => {
  const user = window.user
  const isLoggedIn = !user.is_anonymous
  return (
    <>
    {isLoggedIn ?
      "Show login pagee"
    :
      `Hello ${user.full_name}`
    }
    </>
  )
}

export { ReactApp }
