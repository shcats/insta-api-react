import React, {useState} from "react";
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import TextField from '@mui/material/TextField';
import Stack from '@mui/material/Stack';
import AccountCircle from '@mui/icons-material/AccountCircle';

const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 600,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
  };

function Regform({form}){

    const [open, setOpen] = useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
    console.log(form);

    return (
    <div>
        <Button onClick={handleOpen}> Login </Button> 
        <Button> SignOut </Button>
        <Modal
            open={open}
            onClose={handleClose}
            aria-labelledby="modal-modal-title"
            aria-describedby="modal-modal-description">
            <Box sx={style}>
                <Typography id="modal-modal-title" variant="h6" component="h2">
                   Login as 
                </Typography>
                <Stack direction="row" spacing={3}>
                    <AccountCircle sx={{ color: 'action.active', mr: -1, my: 1, fontSize:40 }} />
                    <TextField
                        required
                        id="outlined-required"
                        label="Required"
                    />
                    <TextField
                        id="outlined-password-input"
                        label="Password"
                        type="password"
                        autoComplete="current-password"
                    />
                    <Button variant="outlined">LOGIN</Button>
                </Stack>
            </Box>
        </Modal>
    </div>
    )
}


export default Regform