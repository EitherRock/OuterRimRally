import React, { useState } from 'react';
import { 
  TextField, 
  Button, 
  Container, 
  Typography, 
  Paper,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions
} from '@mui/material';
import { useNavigate } from 'react-router-dom';
import Header from './header';
import './style.css'

function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [createUsername, setCreateUsername] = useState('');
  const [createPassword, setCreatePassword] = useState('');
  const [confPassword, setConfPassword] = useState('')
  const [cruiserName, setCruiserName] = useState('');
  const [error, setError] = useState('');
  const [errorCreate, setErrorCreate] = useState('')
  const [open, setOpen] = useState(false);
  const navigate = useNavigate();
  const [isLoading, setIsLoading] = useState(false);

  const handleOpen = () => {
    setOpen(true);
    setError('');
  };

  const handleClose = () => {
    setOpen(false);
    setErrorCreate('');
    setCreateUsername('');
    setPassword('');
  }

  const handleCreate = async () => {
    setErrorCreate('');
    try{
      if (createPassword !== confPassword) {
        throw new Error('Passwords do not match!')
      }

      if (!createUsername || !createPassword || !confPassword) {
        throw new Error("Username and password required.");
      }

      // if (!createUsername || !createPassword) {
      //   setErrorCreate('Both username and password are required')
      // }

      console.log(createPassword);
      console.log(createUsername);

      setIsLoading(true);
      const response = await fetch('http://127.0.0.1:8000/racers/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: createUsername,
          password: createPassword,
          // cruiser_name: cruiserName <-- not implemented yet
        }),
      });
      
      if (!response.ok) {
        const errorData = await response.json();
        console.log(errorData);
        if (Array.isArray(errorData.details)){
          const errorMessages = errorData.detail.map(err => err.msg).join(", ");
          throw new Error(errorMessages);
        } else if (typeof errorData.detail === "string") {
            throw new Error(errorData.detail);
        }
        throw new Error("Failed to create account");
      }
      
      alert("Account created Successfully!");
      setOpen(false);
    } catch (error) {
      setErrorCreate(error.message)
    }
    setIsLoading(false);
  };

  const handleLogin = async () => {
    try{
      const formData = new URLSearchParams();
      formData.append('username', username);
      formData.append('password', password);

      setIsLoading(true);
      const response = await fetch('http://127.0.0.1:8000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formData.toString(),
      });

      if (!response.ok) {
        throw new Error('Invalid username or password');
      }

      const data = await response.json();
      
      localStorage.setItem('access_token', data.access_token);
      localStorage.setItem('exp', data.exp);
      console.log(data)
      navigate('/home');

    } catch (error) {
      setError(error.message);
    }
    setIsLoading(false);
  };

  const PasswordField = ({ label, value, onChange }) => (
    <TextField
      label={label}
      type='password'
      fullWidth
      margin='normal'
      variant="outlined"
      value={value}
      onChange={onChange}
    />
  )

  return (
    <div className='app-login'>
      <Header />
      <Container maxWidth="xs" className='login-container'>
        <Paper elevation={3} style={{ padding: '30px', marginTop: '50px' }}>
          <h2 className ='custom-h4'>
            Login
          </h2>
          
          <TextField
            label="Username"
            fullWidth
            margin="normal"
            variant="outlined"
            value={username}
            onChange={(e) => { setUsername(e.target.value); setError(''); }}
          />
          <TextField
            label="Password"
            type="password"
            fullWidth
            margin="normal"
            variant="outlined"
            value={password}
            onChange={(e) => { setPassword(e.target.value); setError(''); }}
          />
          {error && (
            <Typography color='error' variant='body2' align='center'>
              {error}
            </Typography>
          )}
          <Button
            variant='contained'
            color='primary'
            fullWidth
            style={{ marginTop: '20px' }}
            onClick={handleLogin}
            disabled={isLoading} 
          >
            Sign In
          </Button>
          <Button
            variant='contained'
            color='primary'
            fullWidth
            style={{ marginTop: '20px' }}
            onClick={handleOpen}
            disabled={isLoading}
          >
            Create Account
          </Button>
        </Paper>
      </Container>

      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>Create an Account</DialogTitle>
        <DialogContent>
            <TextField 
              label='New Username' 
              fullWidth 
              margin='normal'
              onChange={(e) => { setCreateUsername(e.target.value); setErrorCreate(''); }} 
            />
            <TextField 
              label='New Password' 
              type='password' 
              fullWidth 
              margin='normal'
              onChange={(e) => { setCreatePassword(e.target.value); setErrorCreate(''); }} 
            />
            <TextField 
              label='Confirm Password' 
              type='password' 
              fullWidth 
              margin='normal'
              onChange={(e) => { setConfPassword(e.target.value); setErrorCreate(''); }} 
            />
            <TextField 
              label='Cruiser Name' 
              fullWidth 
              margin='normal' 
              onChange={(e) => { setCruiserName(e.target.value); setErrorCreate(''); }}
            />
        </DialogContent>
        {errorCreate && (
            <Typography color="error" variant="body2" align="center">
              {errorCreate}
            </Typography>
          )}
        <DialogActions>
          <Button 
            onClick={handleClose} 
            color='secondary' 
            variant='contained'
          >
            Cancel
          </Button>
          <Button 
            onClick={handleCreate} 
            disabled={isLoading} 
            color='primary'
            variant='contained'
          >
            Create
          </Button>
        </DialogActions> 
      </Dialog>
    </div>
  );
}

export default LoginPage;