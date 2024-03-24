// Fichier "5-building.js"

export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building && this.evacuationWarningMessage !== 'function') {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  // Getter
  get sqft() {
    return this._sqft;
  }
}
