import { Navigate, Outlet } from 'react-router-dom'
import { jwtDecode } from 'jwt-decode';


const PrivateRoute = () => {
    const token = localStorage.getItem("access_token");

    if (!token) {
        return <Navigate to="/" replace />;
    }

    try {
        const decodedToken = jwtDecode(token);
        const currentTime = Date.now() / 1000;

        if (decodedToken.exp < currentTime) {
            localStorage.removeItem('access_token');
            return <Navigate to="/" replace />
        }
    } catch (error) {
        console.error("Error decoding token:", error);
        localStorage.removeItem('access_token');
        return <Navigate to="/" replace />;
    }

    return <Outlet />;
}

export default PrivateRoute;