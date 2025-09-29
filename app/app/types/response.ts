export interface ILoginResponse {
	session_token: string;
}

export interface IMeResponse {
	username: string;
}

export interface IIAResponse {
	categoria: string;
	justificativa: string;
	resposta_sugerida: string;
	content: string;
}

export interface IListResponse {
	emails: IEmail[];
	total: number;
	offset: number;
	limit: number;
}

export interface IEmail {
	_id: string;
	content: string;
	category: string;
	response: string;
	justification: string;
	created_at: string;
}
