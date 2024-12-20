export type Authorisation = {
    token?: string,
    expiry?: number,
}

export type User = Authorisation &
{
    password?: string,
    username: string,
}

export type Group = Authorisation &
{
    name?: string,
    description?: string,
    id: string,
}


export type StudyTimer =
{
    duration: number;
}

export type Leaderboard = Array<User>;

export type Groups = Array<Group>;

