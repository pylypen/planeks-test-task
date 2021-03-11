export default class ColumnTypesService {
    _apiBase = `/schemas/column/`;

    getResource = async (url) => {
        const res = await fetch(this._apiBase + url);

        if (!res.ok) {
            throw new Error(`
                Could not getch ${url}, received status ${res.status}
            `)
        }

        return await res.json();
    }

    getAllPeople = async () => {
        const res = await this.getResource('types/');
        return res.results.map(this._transformPerson);
    }

    _transformPerson = (person) => {
        return {
            id: person.pk,
            name: person.fields.name,
        };
    }
}