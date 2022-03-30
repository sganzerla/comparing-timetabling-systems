import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Times } from '../api/times';

@Injectable({
    providedIn: 'root'
  })
export class TimeService {

    private baseUrl = `${environment.apiUrl}/times`;

    constructor(private http: HttpClient) { }

    get(id: string): Observable<Times> {
        return this.http.get<Times>(`${this.baseUrl}/${id}`);
    }

    getAll(): Observable<Array<Times>> {
        return this.http.get<Times[]>(this.baseUrl);
    }

    update(item: Times): Observable<Times> {
        return this.http.put<Times>(`${this.baseUrl}/${item['@Id']}`, item);
    }

    create(item: Times): Observable<Times> {
        return this.http.post<Times>(this.baseUrl, item);
    }

    delete(id: string): Observable<any> {
        return this.http.delete(`${this.baseUrl}/${id}`);
    }
}
