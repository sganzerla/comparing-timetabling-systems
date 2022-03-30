import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Resources } from '../api/resources';

@Injectable({
    providedIn: 'root'
  })
export class ResourceService {

    private baseUrl = `${environment.apiUrl}/resources`;

    constructor(private http: HttpClient) { }

    get(id: string): Observable<Resources> {
        return this.http.get<Resources>(`${this.baseUrl}/${id}`);
    }

    getAll(): Observable<Array<Resources>> {
        return this.http.get<Resources[]>(this.baseUrl);
    }

    update(item: Resources): Observable<Resources> {
        return this.http.put<Resources>(`${this.baseUrl}/${item['@Id']}`, item);
    }

    create(item: Resources): Observable<Resources> {
        return this.http.post<Resources>(this.baseUrl, item);
    }

    delete(id: string): Observable<any> {
        return this.http.delete(`${this.baseUrl}/${id}`);
    }
}
