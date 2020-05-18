import { CryptoManager } from "../../../crypto-manager";
import { IHtlcClaimAsset, ITransactionData, SchemaError } from "../../../interfaces";
import { TransactionTools } from "../../transactions-manager";
import { Two } from "../../types";
import { TransactionBuilder } from "./transaction";

export class HtlcClaimBuilder<
    T,
    U extends ITransactionData = ITransactionData,
    E = SchemaError
> extends TransactionBuilder<T, HtlcClaimBuilder<T, U, E>, U, E> {
    public constructor(cryptoManager: CryptoManager<T>, transactionTools: TransactionTools<T, U, E>) {
        super(cryptoManager, transactionTools);
        this.data.type = Two.HtlcClaimTransaction.type;
        this.data.typeGroup = Two.HtlcClaimTransaction.typeGroup;
        this.data.fee = Two.HtlcClaimTransaction.staticFee(cryptoManager);
        this.data.amount = cryptoManager.LibraryManager.Libraries.BigNumber.ZERO;
        this.data.asset = {};
    }

    public htlcClaimAsset(claimAsset: IHtlcClaimAsset): HtlcClaimBuilder<T, U, E> {
        this.data.asset = {
            claim: claimAsset,
        };

        return this;
    }

    public getStruct(): U {
        const struct: U = super.getStruct();
        struct.amount = this.data.amount;
        struct.asset = this.data.asset;
        return struct;
    }

    protected instance(): HtlcClaimBuilder<T, U, E> {
        return this;
    }
}
