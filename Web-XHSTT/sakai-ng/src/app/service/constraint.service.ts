import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Constraints } from '../api/constraints';

@Injectable({
    providedIn: 'root'
  })
export class ConstraintService {

    private baseUrl = `${environment.apiUrl}/constraints`;

    constructor(private http: HttpClient) { }

    get(id: string): Observable<Constraints> {
        return this.http.get<Constraints>(`${this.baseUrl}/${id}`);
    }

    getAll(): Observable<Array<Constraints>> {
        return this.http.get<Constraints[]>(this.baseUrl);
    }

    update(item: Constraints): Observable<Constraints> {
        return this.http.put<Constraints>(`${this.baseUrl}/${item['@Id']}`, item);
    }

    create(item: Constraints): Observable<Constraints> {
        return this.http.post<Constraints>(this.baseUrl, item);
    }

    delete(id: string): Observable<any> {
        return this.http.delete(`${this.baseUrl}/${id}`);
    }
}
