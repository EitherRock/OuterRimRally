import logo from './logo.svg';
import './App.css';
import './style.css'
import Header from './header';
import LoginPage from './login';
import HomePage from './homepage';
import PrivateRoute from './PrivateRoute';
import { Routes, Route } from 'react-router-dom';
import DataFetcher from './dataFetcher';


function App() {
  return (
    <div className="App">
        <Routes>
          <Route path="/" element={<LoginPage />} />
          <Route element={<PrivateRoute />}>
          <Route path="/home" element={<HomePage />} />
          </Route>
        </Routes>
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        {/* <DataFetcher /> */}
        {/* <p>Hellothere welcome to space stuff Login</p> */}
    </div>
  );
}

export default App;
