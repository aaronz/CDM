import {
    CdmAttributeContext,
    cdmAttributeContextType,
    CdmObject
} from '../internal';

/**
 * @internal
 * the description of a new attribute context into which a set of resolved attributes should be placed.
 */
export interface AttributeContextParameters {
    /**
     * @internal
     */
    under: CdmAttributeContext;

    /**
     * @internal
     */
    type: cdmAttributeContextType;

    /**
     * @internal
     */
    name?: string;

    /**
     * @internal
     */
    regarding?: CdmObject;

    /**
     * @internal
     */
    includeTraits?: boolean;
}
