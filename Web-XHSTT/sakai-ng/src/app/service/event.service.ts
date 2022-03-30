import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Events } from '../api/events';

@Injectable()
export class EventService {

    private baseUrl = `${environment.apiUrl}/events`;

    constructor(private http: HttpClient) { }

    get(id: string): Observable<Events> {
        return this.http.get<Events>(`${this.baseUrl}/${id}`);
    }

    getAll(): Observable<Array<Events>> {
        return this.http.get<Events[]>(this.baseUrl);
    }

    update(item: Events): Observable<Events> {
        return this.http.put<Events>(`${this.baseUrl}/${item['@Id']}`, item);
    }

    create(item: Events): Observable<Events> {
        return this.http.post<Events>(this.baseUrl, item);
    }

    delete(id: string): Observable<any> {
        return this.http.delete(`${this.baseUrl}/${id}`);
    }
}
