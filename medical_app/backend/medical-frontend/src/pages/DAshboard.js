import { useEffect, useState } from "react";
import API from "../api/api"; 
import { logoutUser } from "../api/authService"; 

const Dashboard = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchUserProfile = async () => {
      try {
        const response = await API.get("profile/");
        setUser(response.data);
      } catch (error) {
        console.error("Error fetching user profile:", error);
      }
    };

    fetchUserProfile();
  }, []);

  return (
    <div>
      <h2>Dashboard</h2>
      {user ? <p>Welcome, {user.username}!</p> : <p>Loading...</p>}
      <button onClick={logoutUser}>Logout</button>
    </div>
  );
};

export default Dashboard;
