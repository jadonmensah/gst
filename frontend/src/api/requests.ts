import {Authorisation, Group, Groups, User, StudyTimer, Leaderboard} from "./types.ts"

import {urls} from "./urls.ts"

const CREDENTIALS = "same-origin" // may need changing to "include"

export async function Login (user: User): Promise<Authorisation> {

    const response = await window.fetch(urls.LOGIN, {
        method: "POST",
        body: JSON.stringify(user),
        credentials: CREDENTIALS,
    });

    const data = await response.json();
    if (response.ok) {
        const token = data?.token;
        const expiry = data?.expiry;
        if (token && expiry) {
            return { token: token, expiry: Date.parse(expiry) };
        } else {
            return Promise.reject(new Error("Login failed. Try using a different email or password"));
        }
    }

    return Promise.reject(new Error("Login failed. Try using a different email or password"));
    
}

export async function Signup (user: User): Promise<Authorisation> {
    // do signup
    const response = await window.fetch(urls.SIGNUP, {
        method: "POST",
        body: JSON.stringify(user),
        credentials: CREDENTIALS
    });

    if (response.ok) {
        return Login(user);
    } 

    return Promise.reject(new Error("Signup failed. Perhaps an account with that email already exists."))
}

export async function CreateGroup (group: Group): Promise<Group> {
    let auth: Authorisation = {
        token: group?.token
    }
    const response = await window.fetch(urls.CREATE_GROUP, {
        method: "POST",
        headers: {
            "Authorization": "Token " + auth.token,
        },
        body: JSON.stringify(group),
        credentials: CREDENTIALS,
    });

    const data = await response.json();

    if (response.ok) {
        const name = data?.name;
        const id = data?.id;
        const description = data?.description;

        if (id && description && name) {
            return { id: id, name: name, description: description };
        } else {
            return Promise.reject(new Error("Group creation failed."));
        }
    }

    return Promise.reject(new Error("Group creation failed."));   
}

export async function GetGroupInfo (group: Group): Promise<Group> {
    
    const auth: Authorisation = {
        token: group?.token
    }

    const response = await window.fetch(urls.GET_GROUP + "?id=" + group.id, {
       method: "GET",
       headers: {
        "Authorization": "Token " + auth.token,
        },
       credentials: CREDENTIALS, 
    });

    const data = await response.json();
    
    if (response.ok) {
        if (data.name && data.description) {
            return {id: group.id, name: data.name, description: data.description}
        } else {
            return Promise.reject(new Error("Could not find valid group with given id."))
        }
    }

    return Promise.reject(new Error("Could not find valid group with given id."));
}

export async function SetGroupInfo (group: Group): Promise<Group> {
    const auth: Authorisation = {token: group?.token};

    const response = await window.fetch(urls.SET_GROUP + "?id=" + group.id, {
        method: "POST",
        headers: {
            "Authorization": "Token " + auth.token,
        },
        credentials: CREDENTIALS,
    });
    const data = await response.json();
    if (response.ok) {
        if (data.name && data.description) {
            return {id: group.id, name: data.name, description: data.description}
        } else {
            return Promise.reject(new Error("Could not set group info."));
        }
    }
    return Promise.reject(new Error("Could not set group info."));
}

export async function JoinGroup (group: Group): Promise<boolean> {
    const auth: Authorisation = {token: group?.token};

    const response = await window.fetch(urls.JOIN_GROUP + "?id=" + group.id, {
        method: "POST",
        headers: {
            "Authorization": "Token " + auth.token,
        },
        credentials: CREDENTIALS,
    });

    if (response.ok) {
        return true;
    }
    return Promise.reject(new Error("Could not set group info."));
}

export async function LeaveGroup (group: Group): Promise<boolean> {
    const auth: Authorisation = {token: group?.token};
    const response = await window.fetch(urls.LEAVE_GROUP + "?id=" + group.id, {
        method: "POST",
        headers: {
            "Authorization": "Token " + auth.token,
        },
        credentials: CREDENTIALS,
    });

    if (response.ok) {
        return true;
    }
    return Promise.reject(new Error("Could not leave group. Are you authorised?"))
}

export async function StartTimer (auth: Authorisation): Promise<boolean> {
    const response = await window.fetch (urls.START_TIMER, {
        method: "POST",
        headers: {
            "Authorization": "Token " + auth.token,
        },
        credentials: CREDENTIALS,
    });
    if (response.ok) {
        return true;
    }
    return Promise.reject(new Error("Could not start timer. Are you authorised?"))
}

export async function EndTimer (auth: Authorisation): Promise<StudyTimer> {
    const response = await window.fetch (urls.END_TIMER, {
        method: "POST",
        headers: {
            "Authorization": "Token " + auth.token,
        },
        credentials: CREDENTIALS,
    });

    const data = await response.json();

    if (response.ok) {
        if (data.duration) return {duration: data.duration*1000}; // TODO double check whether API response is s or ms.
    }
    return Promise.reject(new Error("Could not end timer. Are you authorised?"))
}

export async function GetLeaderboard (group: Group): Promise<Leaderboard> {
    const auth: Authorisation = {token: group?.token};
    const response = await window.fetch(urls.LEADERBOARD + "?id=" + group.id, {
        method: "GET",
        headers: {
            "Authorization": "Token " + auth.token,
        },
        credentials: CREDENTIALS,
    });
    const data = await response.json();
    if (response.ok) {
        return data;
    }
    return Promise.reject(new Error("Could not get leaderboard. Does this group exist?"))
}

export async function MyGroups (user: User): Promise<Groups> {
    const auth: Authorisation = {token: user?.token};
    const response = await window.fetch(urls.MYGROUPS, {
        method: "GET",
        headers: {
            "Authorization": "Token " + auth.token,
        },
        credentials: CREDENTIALS,
    });
    const data = await response.json();
    if (response.ok) {
        return data;
    }
    return Promise.reject(new Error("Could not get your groups."))
}