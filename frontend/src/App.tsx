import { useState,  } from 'react'
import './App.css'
// TODO basic frontend to test existing API endpoints

function LoginForm() {
  function logIn(e: any) {
    
    e.preventDefault();
    
    let success: boolean = false;
    
    const form = e.target;
    const formData = new FormData(form);
    const formJSON = Object.fromEntries(formData.entries());

    // TODO api call, fix CORS problems

    if (success) setLoggedIn(true);
  }
  return (
    <>
      <p>log in</p>
      <form method="post" onSubmit={logIn}> 
        <input type="email" name="username" id="login_email" placeholder='email'/>
        <input type="password" name="password" id="login_password" placeholder='password'/>
        <button type="submit">log in</button>
      </form>
    </>
  );
}

function SignUpForm() {
  function signUp() {
    let signUpSuccess: boolean = false;
    // TODO send signup API request, determine whether successful
    if (signUpSuccess) {
      let logInSuccess: boolean = false;
      // TODO send login API request with same creds
      if (logInSuccess) setLoggedIn(true);
      // TODO set up stateful auth object
    }
  }
  return (
    <>
      <p>sign up</p>
      <form> 
        <input type="email" name="username" id="signup_email" placeholder='email'/>
        <input type="password" name="password" id="signup_password" placeholder='password' />
        <button onClick={signUp}>sign up</button>
      </form>
    </>
  );
}

function UserHome() {
  let groups: any = [
    { name: "grp1", description: "test", id: "1"},
    { name: "grp2", description: "test2", id: "2"},
    { name: "grp3", description: "test3", id: "3"},
  ];
  const groupCards: any  = groups.map((group: any) => 
    <li key={group.id}>
      {group.name}
      <br />
      {group.description}
    </li>
    )
  return (
    <>
      <button>Toggle studying</button>
      <ul>{groupCards}</ul>
    </>
  );
}

let setLoggedIn: any;

function App() {
  const [loggedIn, setLoggedIn]: [boolean, React.Dispatch<React.SetStateAction<boolean>>] = useState(false);

  return (
    <>
      <h1>gst</h1>
      { loggedIn ? (
        <UserHome /> 
    ) : (
        <>
          <SignUpForm />
          <LoginForm />
        </>
      )}
    </>
  )
}

export default App
